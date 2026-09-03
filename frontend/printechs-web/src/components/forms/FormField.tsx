import type { InputHTMLAttributes, ReactNode, SelectHTMLAttributes, TextareaHTMLAttributes } from "react";

const fieldClass =
  "mt-2 w-full rounded-sm border border-line bg-white px-4 py-2.5 text-sm text-ink shadow-sm transition placeholder:text-slate/70 focus-visible:border-signal focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal/30";

type FormFieldProps = {
  label: string;
  name: string;
  error?: string;
  hint?: string;
  required?: boolean;
  children: ReactNode;
};

export function FormField({
  label,
  name,
  error,
  hint,
  required = false,
  children,
}: FormFieldProps) {
  return (
    <div>
      <label htmlFor={name} className="block text-sm font-semibold text-ink">
        {label}
        {required ? <span className="text-signal-deep"> *</span> : null}
      </label>
      {children}
      {hint && !error ? (
        <p className="mt-1.5 text-xs text-slate">{hint}</p>
      ) : null}
      {error ? (
        <p className="mt-1.5 text-xs font-medium text-accent" role="alert">
          {error}
        </p>
      ) : null}
    </div>
  );
}

type TextInputProps = InputHTMLAttributes<HTMLInputElement> & {
  label: string;
  error?: string;
  hint?: string;
};

export function TextInput({ label, error, hint, id, name, className = "", ...props }: TextInputProps) {
  const fieldName = name ?? id ?? label.toLowerCase().replace(/\s+/g, "-");
  return (
    <FormField label={label} name={fieldName} error={error} hint={hint} required={props.required}>
      <input id={fieldName} name={fieldName} className={`${fieldClass} ${className}`} {...props} />
    </FormField>
  );
}

type TextAreaProps = TextareaHTMLAttributes<HTMLTextAreaElement> & {
  label: string;
  error?: string;
  hint?: string;
};

export function TextArea({ label, error, hint, id, name, className = "", ...props }: TextAreaProps) {
  const fieldName = name ?? id ?? label.toLowerCase().replace(/\s+/g, "-");
  return (
    <FormField label={label} name={fieldName} error={error} hint={hint} required={props.required}>
      <textarea
        id={fieldName}
        name={fieldName}
        className={`${fieldClass} min-h-[120px] resize-y ${className}`}
        {...props}
      />
    </FormField>
  );
}

type SelectInputProps = SelectHTMLAttributes<HTMLSelectElement> & {
  label: string;
  error?: string;
  hint?: string;
  options: { value: string; label: string }[];
};

export function SelectInput({
  label,
  error,
  hint,
  options,
  id,
  name,
  className = "",
  ...props
}: SelectInputProps) {
  const fieldName = name ?? id ?? label.toLowerCase().replace(/\s+/g, "-");
  return (
    <FormField label={label} name={fieldName} error={error} hint={hint} required={props.required}>
      <select id={fieldName} name={fieldName} className={`${fieldClass} ${className}`} {...props}>
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </FormField>
  );
}
