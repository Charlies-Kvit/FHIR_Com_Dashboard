<script lang="ts">
  import { Modal } from "@/shared/ui";
  import type { Account, Summary } from "@/entities/account";
  import Preview from "./Preview.svelte";
  import ShowMore from "./ShowMore.svelte";
  import Chart from "./Chart.svelte";
  import { EditAccount } from "..";

  let { account } = $props<{ account: Account }>();

  let active_summary_index = $state(0);
  let summaries: undefined | Summary[] = $state(undefined);
  let active_summary = $derived.by(() => {
    if (summaries == undefined) return undefined;
    return summaries[active_summary_index];
  });
  account.summary.then((v: Summary[] | undefined) => {
    summaries = v;
  });
  let show_more = $state(false);
  let show_settings = $state(false);
</script>

<Modal bind:open={show_settings}>
  <EditAccount {account}></EditAccount>
</Modal>
<Modal bind:open={show_more}>
  <ShowMore {...account} summary={active_summary}></ShowMore>
</Modal>
<article
  class="card bg-base-100 card-bordered border-base-300 flex flex-row p-6 h-[390px] w-full max-w-[1060px]"
>
  <Chart {summaries} bind:active_summary_index></Chart>
  <div class="divider mx-6 divider-horizontal"></div>
  <Preview
    {...account}
    summary={active_summary}
    onmore={() => (show_more = true)}
    onsettings={() => (show_settings = true)}
    summary_index={active_summary_index}
  ></Preview>
</article>
