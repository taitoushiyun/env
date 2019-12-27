from gym.envs.registration import register

register(
    id='2DNavigation-v0',
    entry_point='navigation.envs:Navigation2DEnv',
    # max_episode_steps=100

)
