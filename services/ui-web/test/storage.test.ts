// Tests the browser store: JSON under the lugha. prefix, and no throwing when storage fails.
import { describe, expect, it } from "vitest";
import { makeStore } from "../src/lib/storage";

class Memory {
  data = new Map<string, string>();
  getItem(k: string) {
    return this.data.get(k) ?? null;
  }
  setItem(k: string, v: string) {
    this.data.set(k, v);
  }
  removeItem(k: string) {
    this.data.delete(k);
  }
  get length() {
    return this.data.size;
  }
  key(i: number) {
    return [...this.data.keys()][i] ?? null;
  }
}

const broken = {
  getItem(): string | null {
    throw new Error("SecurityError");
  },
  setItem() {
    throw new Error("QuotaExceededError");
  },
  removeItem() {
    throw new Error("SecurityError");
  },
  get length(): number {
    throw new Error("SecurityError");
  },
  key(): string | null {
    throw new Error("SecurityError");
  },
};

describe("store", () => {
  it("keeps and gives back JSON values under the lugha. prefix", () => {
    const m = new Memory();
    const s = makeStore(m);
    expect(s.set("a", { x: [1, 2] })).toBe(true);
    expect(s.get("a")).toEqual({ x: [1, 2] });
    expect([...m.data.keys()]).toEqual(["lugha.a"]);
    s.remove("a");
    expect(s.get("a")).toBeNull();
  });

  it("gives null for a missing key or a value that isn't JSON", () => {
    const m = new Memory();
    m.setItem("lugha.bad", "{nope");
    const s = makeStore(m);
    expect(s.get("missing")).toBeNull();
    expect(s.get("bad")).toBeNull();
  });

  it("keeps nothing, without throwing, when storage fails or is missing", () => {
    for (const s of [makeStore(broken), makeStore(null)]) {
      expect(s.set("a", 1)).toBe(false);
      expect(s.get("a")).toBeNull();
      expect(() => s.remove("a")).not.toThrow();
      expect(() => s.removeStarting("a")).not.toThrow();
    }
  });

  it("removes every key under the lugha. prefix that starts with a given prefix, and nothing else", () => {
    const m = new Memory();
    for (const k of ["lugha.step.a/b/c", "lugha.step.d/e/f", "lugha.progress", "other.step.x"]) m.setItem(k, "1");
    makeStore(m).removeStarting("step.");
    expect([...m.data.keys()].sort()).toEqual(["lugha.progress", "other.step.x"]);
  });
});
