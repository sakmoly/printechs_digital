import type { QuoteOption } from "@/types/quote-config";

const fieldClass =
  "mt-2 w-full appearance-none rounded-sm border border-line bg-white bg-[length:12px] bg-[right_0.9rem_center] bg-no-repeat px-4 py-2.5 text-sm text-ink shadow-sm transition placeholder:text-slate/70 focus-visible:border-product-icon focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-product-icon/20";

const selectChevron =
  "bg-[url('data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2712%27 height=%278%27 fill=%27none%27 viewBox=%270 0 12 8%27%3E%3Cpath stroke=%27%230056B3%27 stroke-linecap=%27round%27 stroke-width=%271.5%27 d=%27m1 1.5 5 5 5-5%27/%3E%3C/svg%3E')]";

function groupOptions(options: QuoteOption[]) {
  const groups: { title?: string; options: QuoteOption[] }[] = [];
  options.forEach((option) => {
    const title = option.group?.trim() || undefined;
    const last = groups[groups.length - 1];
    if (last && last.title === title) {
      last.options.push(option);
      return;
    }
    groups.push({ title, options: [option] });
  });
  return groups;
}

export function QuoteConfigurationFields({
  options,
  sectionTitle = "Configuration",
  sectionDescription = "Select the options that match your site. Required fields are marked.",
}: {
  options: QuoteOption[];
  sectionTitle?: string;
  sectionDescription?: string;
}) {
  if (!options.length) {
    return null;
  }

  return (
    <section>
      <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
        {sectionTitle}
      </p>
      <p className="mt-2 text-sm leading-relaxed text-slate">{sectionDescription}</p>
      <div className="mt-5 space-y-6">
        {groupOptions(options).map((group) => (
          <div key={group.title || group.options.map((option) => option.id).join("-")}>
            {group.title ? (
              <p className="mb-3 text-sm font-semibold text-ink">{group.title}</p>
            ) : null}
            <div className="grid gap-5 sm:grid-cols-2">
              {group.options.map((option) => {
                const fieldName = `config.${option.label}`;
                if (option.type === "checkbox") {
                  return (
                    <div key={option.id} className="sm:col-span-2">
                      <p className="text-sm font-semibold text-ink">
                        {option.label}
                        {option.required ? <span className="text-product-icon"> *</span> : null}
                      </p>
                      <div className="mt-3 flex flex-wrap gap-2">
                        {option.choices.map((choice) => (
                          <label
                            key={choice}
                            className="inline-flex cursor-pointer items-center gap-2 rounded-sm border border-line bg-white px-3 py-2 text-sm text-ink shadow-sm transition hover:border-product-icon/40 has-[:checked]:border-product-icon has-[:checked]:bg-product-icon/5"
                          >
                            <input
                              type="checkbox"
                              name={fieldName}
                              value={choice}
                              className="h-4 w-4 rounded-sm border-line text-product-icon focus:ring-product-icon/30"
                            />
                            {choice}
                          </label>
                        ))}
                      </div>
                    </div>
                  );
                }

                return (
                  <label key={option.id} className="block">
                    <span className="text-sm font-semibold text-ink">
                      {option.label}
                      {option.required ? <span className="text-product-icon"> *</span> : null}
                    </span>
                    <select
                      name={fieldName}
                      required={option.required}
                      defaultValue=""
                      className={`${fieldClass} ${selectChevron} pr-10`}
                    >
                      <option value="" disabled>
                        Select…
                      </option>
                      {option.choices.map((choice) => (
                        <option key={choice} value={choice}>
                          {choice}
                        </option>
                      ))}
                    </select>
                  </label>
                );
              })}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export function formatQuoteConfiguration(formData: FormData): string {
  const lines: string[] = [];
  Array.from(formData.entries()).forEach(([key, value]) => {
    if (!key.startsWith("config.") || !String(value).trim()) {
      return;
    }
    const label = key.replace(/^config\./, "");
    lines.push(`${label}: ${String(value)}`);
  });
  return lines.length ? `Configuration\n${lines.join("\n")}` : "";
}
