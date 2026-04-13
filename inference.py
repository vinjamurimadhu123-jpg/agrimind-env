from env.environment import AgriMindEnv
print("[START]")

from env.environment import AgriMindEnv

env = AgriMindEnv()
obs = env.reset()

action = {
    "crop": "tomato",
    "fertilizer": "organic",
    "irrigation": "drip",
    "sell_time": "wait"
}

obs, reward, done, info = env.step(action)

print("[STEP]", reward)
print("[END]", reward)
