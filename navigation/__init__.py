from gym.envs.registration import register

register(
    '2DNavigation-v0',
    entry_point='envs.navigation:Navigation2DEnv',
    # max_episode_steps=100
    kwargs={'log_level': 'ERROR'},
)
