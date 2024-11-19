import { browser } from "$app/environment";
import { get, writable } from "svelte/store";
export type Dashboard = { name: string, id?: number }


const createDashboardStore = () => {
  let { subscribe, set, update } = writable<Dashboard[]>([])

  const load = () => {
    fetch('/api/groups')
      .then(
        response => response.json()
          .then(result => set(result.groups))
      )
  }
  if (browser) load()
  subscribe((v) => {
    if (v.length != 0 && get(selected_dashboard) == null) {
      selected_dashboard.select(v[0])
    }
  })

  const add = (dashboard: Dashboard) => {
    fetch("/api/groups", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dashboard)
    }).then(res => {
      load()
      console.log("Request complete! response:", res);
    })
  }
  const update_dashboard = (dashboard_old: Dashboard, dashboard_new: Dashboard) => {
    fetch("/api/groups/" + dashboard_old.id, {
      method: "PUT",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dashboard_new)
    }).then(res => {
      load()
      console.log("Request complete! response:", res);
    });
  }
  const remove = (dashboard: Dashboard) => {
    if (get(selected_dashboard) == dashboard) selected_dashboard.select(null)
    fetch("/api/groups/" + dashboard.id, {
      method: "DELETE",
    }).then(res => {
      load()
      console.log("Request complete! response:", res);
    });
  }

  if (browser) load()

  return { subscribe, add, load, update: update_dashboard, remove }
}
export let dashboards = createDashboardStore()

const createSelectedDashbordStore = () => {
  const store = writable<Dashboard | null>(null)
  const { subscribe, set } = store
  const select = (new_dashboard: Dashboard | null) => {
    if (new_dashboard == null) set(null)
    else if (new_dashboard.id != get(store)?.id) set(new_dashboard)
  }
  return { subscribe, select }
}
export const selected_dashboard = createSelectedDashbordStore()
