import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const body = await request.json().catch(() => null);
  if (!body?.name || !body?.email) {
    return NextResponse.json({ ok: false }, { status: 400 });
  }

  const erpnextUrl =
    process.env.ERPNEXT_URL ||
    process.env.NEXT_PUBLIC_ERPNEXT_URL ||
    "https://printechs.com";

  try {
    const response = await fetch(`${erpnextUrl.replace(/\/$/, "")}/api/method/printechs_digital.api.lead.submit_lead`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify({
        cmd: "printechs_digital.api.lead.submit_lead",
        ...body,
        context: {
          ...(body.context || {}),
          sourceUrl:
            body.context?.sourceUrl ||
            body.context?.attribution?.landing_page ||
            undefined,
        },
      }),
    });

    if (response.ok) {
      const payload = (await response.json().catch(() => null)) as
        | { message?: { ok?: boolean; reference?: string; message?: string } }
        | null;
      const message = payload?.message;
      if (message?.ok) {
        return NextResponse.json({
          ok: true,
          reference: message.reference || "WEB-LEAD",
          message: message.message || "Thank you. Your request has been received.",
        });
      }
    }
  } catch {
    // Fall through — still accept the request so the form does not block the customer.
  }

  return NextResponse.json({
    ok: true,
    reference: "WEB-LEAD",
    message: "Thank you. Your request has been received.",
  });
}
