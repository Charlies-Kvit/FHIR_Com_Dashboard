<script lang="ts">
  import EditForm from "$lib/components/EditForm.svelte";
  import { dashboards } from "$lib/store/dashboard.store";
  import { type Person, persons } from "$lib/store/person.store";

  let { person } = $props<{ person: Person }>();
  let { group_id, avatar_url, name, email } = person;

  const update_person = () => {
    persons.update(person, { group_id, avatar_url, name, email });
  };
  const delete_person = () => {
    persons.remove(person);
  };
</script>

<EditForm
  title="Edit person"
  oncomplete={update_person}
  ondelete={delete_person}
>
  <select class="select" name="dashboard" bind:value={group_id}>
    {#each $dashboards as dashboard}
      <option value={dashboard.id}>{dashboard.name}</option>
    {/each}
  </select>
  <input
    class="input"
    type="text"
    bind:value={avatar_url}
    placeholder="Upload image"
  />
  <input class="input" type="text" bind:value={name} placeholder="Name" />
  <input class="input" type="email" bind:value={email} placeholder="E-mail" />
</EditForm>
