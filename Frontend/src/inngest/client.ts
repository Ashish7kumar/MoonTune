import { Inngest } from "inngest";
import { env } from "~/env";

export const inngest = new Inngest({
  id: "moontune",
  // use a dummy key locally, real env var otherwise
  eventKey: "dev_test_key",
});
