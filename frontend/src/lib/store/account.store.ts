import { browser } from "$app/environment";
import type { Dashboard } from "$lib/store/dashboard.store.ts";
import { writable, get } from "svelte/store";

export class Account {
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
    if (this.#summary.length != 0)
      return new Promise((resolve, _) => resolve(this.#summary));

    return fetch("/api/parsing", {
      method: "POST",
      body: JSON.stringify({
        emails: [this.email],
        zulip_ids: [this.zulip_id],
      }),
    }).then((r) => {
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
const createAccountsStore = () => {
  const store = writable<Account[]>([]);
  const { subscribe, set, update } = store;

  const load = async () => {
    fetch("/api/accounts").then((response) =>
      response
        .json()
        .then((result) =>
          set(
            result.accounts.map((v: Omit<Account, "summary">) =>
              Account.from_object(v),
            ),
          ),
        ),
    );
  };
  if (browser) load();

  const add_account = async (account: Omit<Account, "id" | "summary">) => {
    const res = await fetch("/api/accounts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(account),
    });

    if (res.ok) {
      const account: { account: Omit<Account, "summary"> } = await res.json();
      update((store) => [...store, Account.from_object(account.account)]);
      console.log("Account added", account.account);
    }
  };
  const update_account = async (account_new: Omit<Account, "summary">) => {
    const res = await fetch("/api/accounts/" + account_new.id, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(account_new),
    });
    if (res.ok) {
      console.log("Update account", res);
      // const account_new: Account = Account.from_object(await res.json())
      // update(
      //   store => {
      //     console.log("Store updated")
      //     const next_store = store.filter((acc) => acc.id != account_new.id)
      //     return [...next_store, account_new]
      //   }
      // )
      load();
    }
  };
  const remove_account = (person: Account) => {
    fetch("/api/accounts/" + person.id, {
      method: "DELETE",
    }).then((res) => {
      console.log("Request complete! response:", res);
      load();
    });
  };
  return {
    subscribe,
    add: add_account,
    update: update_account,
    remove: remove_account,
  };
};

export const accounts = createAccountsStore();

export type Summary = {
  timestamp: number;
  id: number;
  account_id: number;
  title: string;
  account_post_count: number;
  url: string;
  text: string;
};
let response: Summary[] = [
  {
    timestamp: 1722638567,
    title: "Smart quotes in output",
    id: 1,
    url: "https://chat.fhir.org/#narrow/stream/179252-ig-creation/topic/Smart.20quotes.20in.20output",
    text: 'To provide a summary of the thread and Grahame Grieve\'s post, as well as key advice from other interlocutors, I will summarize the content from the specified thread on chat.fhir.org. Here is the requested summary:\n\n### Topic Summary\nThe thread titled "Smart quotes in output" discusses the issue of smart quotes appearing in FHIR output, specifically in the context of SMART quotes. The participants discuss how to handle and prevent the appearance of these quotes in FHIR output.\n\n### Grahame Grieve\'s Post Summary\nGrahame Grieve\'s post in this thread focuses on the issue of smart quotes in FHIR output and how to handle them. He explains that the issue is due to the way HTML is rendered and how browsers handle quotes. He also provides a solution to prevent smart quotes from appearing in FHIR output.\n\n### Key Advice from Other Interlocutors\n1. **Author: Ward Weistra**\n   - "The issue is that HTML is rendering the quotes as smart quotes. You can use HTML entities to prevent this. For example, `&quot;` instead of `"`."\n\n2. **Author: Grahame Grieve**\n   - "The problem is that browsers are interpreting the quotes as smart quotes. You can use the `html` attribute in the FHIR output to prevent this. For example, `html="false"`."\n\n3. **Author: Grahame Grieve**\n   - "The issue is due to the way HTML is rendered. You can use a library like `jsoup` to parse the HTML and replace the smart quotes with regular quotes."\n\n4. **Author: Ward Weistra**\n   - "You can also use a library like `StringEscapeUtils` to escape the quotes in the output."\n\n5. **Author: Grahame Grieve**\n   - "The best solution is to use a library that can handle HTML parsing and quote escaping. This will ensure that smart quotes do not appear in the output."\n\nThese summaries and advice should help you understand the key points and solutions discussed in the thread.',
    account_id: 1,
    account_post_count: 25,
  },
  {
    timestamp: 1723070509,
    title: "Last minute changes to R6 prior to the ballot",
    id: 2,
    url: "https://chat.fhir.org/#narrow/stream/179192-fmg/topic/Last.20minute.20changes.20to.20R6.20prior.20to.20the.20ballot",
    text: '**Topic Summary**\nThe thread on "Last minute changes to R6 prior to the ballot" discusses the final modifications to the Release 6 (R6) of the FHIR standard before it goes to ballot. The community discusses the changes, their implications, and the need for clarity on certain aspects. The thread is part of the FHIR Implementers stream, where developers and implementers share insights and concerns about the standard.\n\n**Grahame Grieve Posts Summary**\nGrahame Grieve, a key figure in the FHIR community, posted a summary of the changes and their context. He highlighted the importance of understanding the changes and their impact on the standard. He emphasized the need for thorough testing and feedback before the ballot to ensure the standard is robust and effective.\n\n**Advice from Other Interlocutors**\n\n1. **Author: John Doe**\n   "It\'s crucial to review the changes carefully and provide feedback. This will help in refining the standard before it becomes a normative standard."\n\n2. **Author: Jane Smith**\n   "Make sure to test the changes thoroughly to identify any potential issues. This will help in ensuring the standard is stable and reliable."\n\n3. **Author: Bob Johnson**\n   "Consider the implications of the changes on existing implementations. This will help in minimizing disruptions and ensuring a smooth transition."\n\n4. **Author: Sarah Lee**\n   "Provide constructive feedback on the changes. This will help in improving the standard and making it more effective for implementers."\n\n5. **Author: Michael Brown**\n   "Don\'t hesitate to ask questions if you\'re unsure about the changes. This will help in clarifying any doubts and ensuring a better understanding of the standard."\n\nThese summaries and advice are based on the thread "Last minute changes to R6 prior to the ballot" on the FHIR Implementers stream.',
    account_id: 1,
    account_post_count: 18,
  },
  {
    timestamp: 1722739321,
    title: "Undefined Language",
    id: 3,
    url: "https://chat.fhir.org/#narrow/stream/437028-terminology-service-test-cases/topic/Undefined.20Language",
    text: 'I\'d be happy to help you with that. Here is a summary of the thread and the posts by Grahame Grieve, along with some advice from other interlocutors:\n\n### Topic Summary\nThe thread discusses test cases for terminology services in FHIR. The participants discuss the importance of clear and consistent terminology to ensure interoperability and the need for standardized testing procedures to validate terminology services.\n\n### Grahame Grieve Posts Summary\nGrahame Grieve emphasizes the importance of defining clear terminology and the need for standardized testing procedures to ensure interoperability. He also highlights the challenges of testing terminology services and the need for a comprehensive approach to address these challenges.\n\n### Advice from Other Interlocutors\n1. **Author: John Doe**\n   - "It\'s crucial to define clear terminology and ensure that all stakeholders agree on the definitions. This will help in avoiding misunderstandings and ensuring seamless communication."\n\n2. **Author: Jane Smith**\n   - "Standardized testing procedures are essential to validate terminology services. We should focus on creating a comprehensive testing framework that covers all aspects of terminology services."\n\n3. **Author: Michael Brown**\n   - "Clear documentation and well-defined terminology are key to successful implementation of terminology services. We should prioritize creating detailed documentation that covers all aspects of terminology services."\n\n4. **Author: Emily Chen**\n   - "Interoperability is crucial in healthcare, and clear terminology is a fundamental aspect of it. We should focus on creating a standardized terminology that can be easily understood and implemented across different systems."\n\n5. **Author: David Lee**\n   - "Testing terminology services should not be limited to a single system or environment. We should conduct comprehensive testing across different systems and environments to ensure that the terminology services work seamlessly."\n\n### Marked Names\n- **Grahame Grieve**: Grahame Grieve posts summary\n- **John Doe**: Author: John Doe\n- **Jane Smith**: Author: Jane Smith\n- **Michael Brown**: Author: Michael Brown\n- **Emily Chen**: Author: Emily Chen\n- **David Lee**: Author: David Lee',
    account_id: 1,
    account_post_count: 10,
  },
  {
    timestamp: 1722836538,
    title: "R6 snapshot",
    id: 4,
    url: "https://chat.fhir.org/#narrow/stream/179165-committers/topic/R6.20snapshot",
    text: "I'd be happy to help you with that. Please provide the sources you have read, and I will summarize the thread for you.",
    account_id: 1,
    account_post_count: 7,
  },
  {
    timestamp: 1722857783,
    title: "Using DICOM Enums in FHIR",
    id: 5,
    url: "https://chat.fhir.org/#narrow/stream/179202-terminology/topic/Using.20DICOM.20Enums.20in.20FHIR",
    text: '**Topic Summary:**\nThe thread discusses using DICOM enums in FHIR. Participants share their experiences and challenges in mapping DICOM enums to FHIR, and they seek guidance on how to handle these mappings effectively.\n\n**Grahame Grieve Posts Summary:**\nGrahame Grieve emphasizes the importance of understanding the context and usage of DICOM enums in FHIR. He suggests that the key is to identify the specific DICOM enum that is relevant to the FHIR resource being used and then map it accordingly. He also highlights the need for clear documentation and community support to address these issues.\n\n**Advice from Other Interlocutors:**\n\n1. **Author: Michael O\'Connor**\n   "When mapping DICOM enums, ensure you understand the specific context and usage of each enum. This will help in creating accurate and meaningful mappings."\n\n2. **Author: John Moehrke**\n   "Use the FHIR terminology service to manage and map DICOM enums. This will help in maintaining consistency and reducing errors."\n\n3. **Author: David Hay**\n   "In complex mappings, consider creating custom value sets for DICOM enums. This will allow for more flexibility and better management of the mappings."\n\n4. **Author: Grahame Grieve**\n   "When dealing with DICOM enums, always refer to the DICOM standard for the specific meanings and contexts of each enum. This will ensure accurate and consistent mappings."\n\n5. **Author: Michael O\'Connor**\n   "For large-scale implementations, consider using a terminology server to manage and distribute DICOM enum mappings. This will help in maintaining consistency and reducing errors."\n\nThese summaries and advice should provide a comprehensive overview of the discussion and the key points raised in the thread.',
    account_id: 1,
    account_post_count: 7,
  },
]; // Default value
