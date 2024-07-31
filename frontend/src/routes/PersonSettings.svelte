<script lang="ts">
  import { dashboards, persons, type Person } from "$lib/store.svelte";
  import EditForm from "$lib/components/EditForm.svelte";

  let { person } = $props<{ person: Person }>();
  let { group_id, avatar_url, name, email } = person;

  const update_person = () => {
    persons.update(person, { group_id, avatar_url, name, email });
  };
  const delete_person = () => {
    persons.delete(person);
  };
</script>

<EditForm
  title="Edit person"
  oncomplete={update_person}
  ondelete={delete_person}
>
  <select class="select" name="dashboard" bind:value={group_id}>
    {#each dashboards.value as dashboard, i}
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
