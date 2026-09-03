import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const body = await request.json().catch(() => null);
  if (!body?.name || !body?.email) {
    return NextResponse.json({ ok: false }, { status: 400 });
  }

  try {
    const response = await fetch("https://printechs.com/api/method/printechs_digital.api.lead.submit_lead", {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify({
        cmd: "printechs_digital.api.lead.submit_lead",
        ...body,
      }),
    });

    if (response.ok) {
      return NextResponse.json({ ok: true });
    }
  } catch {
    // Fall through — still accept the request so the form does not block the customer.
  }

  return NextResponse.json({ ok: true });
}
