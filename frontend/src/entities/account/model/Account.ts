import type Summary from "./Summary";

export default class Account {
  constructor(
    public avatar_url: string,
    public name: string,
    public email: string,
    public group_id: number,
    public id: number,
    public zulip_id: number,
  ) {}
  static from_object(obj: {
    avatar_url: string;
    name: string;
    email: string;
    group_id: number;
    id: number;
    zulip_id: number;
  }) {
    return new Account(
      obj.avatar_url,
      obj.name,
      obj.email,
      obj.group_id,
      obj.id,
      obj.zulip_id,
    );
  }

  #summary: Summary[] = [];
  public get summary(): Promise<Summary[] | undefined> {
    if (this.#summary.length != 0) return Promise.resolve(this.#summary);

    return fetch("/api/parsing", {
      method: "POST",
      body: JSON.stringify({
        emails: [this.email],
        zulip_ids: [this.zulip_id],
      }),
      headers: {
        "Content-Type": "application/json",
      },
    }).then((r) => {
      console.log(r);
      if (r.ok) {
        return fetch("/api/parsing/" + this.id).then(async (v) => {
          if (v.ok) {
            this.#summary = (await v.json())[this.email].slice(1, 6);
            return this.#summary;
          }
          this.#summary = [];
        });
      } else {
        console.log(`Can't get parsing of account`, this);
        return undefined;
      }
    });
  }
}
