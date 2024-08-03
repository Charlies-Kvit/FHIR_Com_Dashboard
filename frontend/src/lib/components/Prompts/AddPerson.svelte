<script lang="ts">
  import { type Person, persons } from "$lib/store/person.store";
  import { type Dashboard } from "$lib/store/dashboard.store";
  import EditForm from "$lib/components/EditForm.svelte";

  let { dashboard, onadd } = $props<{
    dashboard: Dashboard;
    onadd: () => void;
  }>();
  let person: Person = {
    avatar_url: "",
    name: "",
    email: "",
    group_id: dashboard.id,
  };

  const add_person = () => {
    persons.add(person);
    onadd();
  };
</script>

<EditForm title="Add person" oncomplete={add_person}>
  <input
    class="input"
    type="text"
    bind:value={person.avatar_url}
    placeholder="Upload image"
  />
  <input
    class="input"
    type="text"
    bind:value={person.name}
    placeholder="Name"
  />
  <input
    class="input"
    type="email"
    bind:value={person.email}
    placeholder="E-mail"
  />
</EditForm>
