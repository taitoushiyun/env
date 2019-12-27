import gym
import navigation

env = gym.make('2DNavigation-v0')
obs = env.reset()
step = 0
while True:
    step += 1
    print(step)
    action = env.action_space.sample()
    cur_obs, reward, done, info = env.step(action)
    if done or step == 50:
        break
