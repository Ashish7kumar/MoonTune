import { Inngest } from "inngest";
import { env } from "~/env.js";

export const inngest = new Inngest({
  id: "moontune",
  eventKey: env.INNGEST_EVENT_KEY, 
});