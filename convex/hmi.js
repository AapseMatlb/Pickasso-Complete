
import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

export const getStatus = query(async (ctx) => {
  const status = await ctx.db.query("status").first();
  return status || { task: "Idle", battery: 100 };
});

export const updateStatus = mutation({
  args: { task: v.string(), battery: v.number() },
  handler: async (ctx, args) => {
    await ctx.db.insert("status", { task: args.task, battery: args.battery });
  },
});

export const logAction = mutation({
  args: { action: v.string(), reason: v.string() },
  handler: async (ctx, args) => {
    await ctx.db.insert("action_logs", { action: args.action, reason: args.reason, timestamp: Date.now() });
  },
});

export const getActionLogs = query(async (ctx) => {
  return await ctx.db.query("action_logs").order("desc").take(10);
});
