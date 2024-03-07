import os
import time
import gym
import numpy as np
import matplotlib.pyplot as plt

from stable_baselines3 import TD3
from stable_baselines3.td3.policies import MlpPolicy
from stable_baselines3 import results_plotter
from VecMonitor import VecMonitor
from stable_baselines3.results_plotter import load_results, ts2xy
#from stable_baselines.common.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise, AdaptiveParamNoiseSpec
from stable_baselines3.common.noise import NormalActionNoise
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.cmd_util import make_vec_env
from myns3env import myns3env
import csv

time_steps = 22500
episode_steps =250
episode_number = int(time_steps/episode_steps)


# Create log dir
log_dir = "tmp_{}/".format(int(time.time()))
os.makedirs(log_dir, exist_ok=True)

# Create and wrap the environment
# Instantiate the env
env = myns3env()
# wrap it
env = make_vec_env(lambda: env, n_envs=1)

env = VecMonitor(env, log_dir)
#env = VecNormalize(env, norm_obs=True, norm_reward=False, clip_obs=100.)
# the noise objects for TD3

n_actions = env.action_space.shape[-1]

action_noise = NormalActionNoise(mean=np.zeros(n_actions), sigma=0.1 * np.ones(n_actions))

model = TD3(MlpPolicy, env, action_noise=action_noise, verbose=1, tensorboard_log="./TD3_ped_veh_tensorboard/")

model = TD3.load ("TD3_ped_veh_r1_1680426721")         #mew =5 
#model = TD3.load ("TD3_ped_veh_r1_1679984265")      # mew = 2

# Test the agent
print("######################Testing#####################")
episode_rewards = []
episode_throughputs = []
Step_rewards = []
Step_throughputs = []

for i in range(1):
    reward_sum = 0
    throughput_sum = 0
    obs = env.reset()
    for j in range(episode_steps):
        print("Test: Step : {} | Episode: {}".format(j, i))

        if(j % 10 == 0):
        	action, _states = model.predict(obs)
        	print(action)
        obs, rewards, dones, info = env.step(action)
        #throughput = env.ret_throughput();
        Step_rewards.append(rewards)
        #Step_throughputs.append(throughput)
        reward_sum += rewards
        #throughput_sum += throughput
    episode_rewards.append(reward_sum)
    #episode_throughputs.append(throughput_sum)
episode_rewards = [x / episode_steps for x in episode_rewards]
#episode_throughputs = [y / episode_steps for y in episode_throughputs]
#DDQN_action_sum = DDQN_action_sum/(6*episode_steps )

#for k in range(episode_steps):
#       episode_rewards.append(reward_sum)
#episode_rewards = [x / episode_steps for x in episode_rewards]

episode_rewards_0 = []
Step_rewards0 = []
episode_throughputs_0 = []
Step_throughputs0 = []

for i in range(1):
    reward_sum0 = 0
    throughput_sum0 = 0
    obs = env.reset()
    for j in range(episode_steps):
        action_0=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
       
        print("Baseline: Step : {} | Episode: {}".format(j, i))
        obs, rewards, dones, info = env.step(action_0)
        #throughput = env.ret_throughput();
        reward_sum0 += rewards
        #throughput_sum0 += throughput
        Step_rewards0.append(rewards)
        #Step_throughputs0.append(throughput)


    episode_rewards_0.append(reward_sum0)
    #episode_throughputs_0.append(throughput_sum0)

episode_rewards_0 = [x / episode_steps for x in episode_rewards_0]
#episode_throughputs_0 = [y / episode_steps for y in episode_throughputs_0]
#for k in range(episode_steps):
#       episode_rewards_0.append(reward_sum0)

#episode_rewards_0 = [x / episode_steps for x in episode_rewards_0]
#print("MIMO action percentage {}".format(DDQN_action_sum))
Result_row=[]
with open('R1_' + 'TD3_step' + format(int(time.time()))+'.csv', 'w', newline='') as BSCSV:

                     results_writer = csv.writer(BSCSV, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)

                     Result_row.clear()

                     Result_row=Result_row+episode_rewards_0

                     results_writer.writerow(Result_row)

                     Result_row.clear()

                     Result_row=Result_row+Step_rewards0

                     results_writer.writerow(Result_row)

                     Result_row.clear()

                     Result_row=Result_row+episode_rewards

                     results_writer.writerow(Result_row)

                     Result_row.clear()

                     Result_row=Result_row+Step_rewards

                     results_writer.writerow(Result_row)
              
BSCSV.close()





fig1, ax = plt.subplots()
ln1, = plt.plot(np.repeat(episode_rewards,episode_steps,axis=0), label='TD3 Average')
ln1, = plt.plot(np.repeat(episode_rewards_0,episode_steps,axis=0), label='Baseline Average')
ln1, = plt.plot(Step_rewards, label='TD3')
ln1, = plt.plot(Step_rewards0, label='Baseline')

legend = ax.legend(loc='upper left', shadow=True, fontsize='x-small')
plt.xlabel("Step")
plt.ylabel("Average Overall throughput")
#plt.title('Comparing step reward: TD3 vs. baseline')
plt.savefig('TD3_0CIO_{}.png'.format(int(time.time())))




#fig2, ax2 = plt.subplots()
#ln2, = plt.plot(episode_throughputs, label='TD3 Average')
#ln2, = plt.plot(episode_throughputs_0, label='Baseline Average')
#ln2, = plt.plot(Step_throughputs, label='TD3')
#ln2, = plt.plot(Step_throughputs0, label='Baseline')

#legend = ax2.legend(loc='upper left', shadow=True, fontsize='x-small')
#plt.xlabel("Step")
#plt.ylabel("Average Overall Throughput")
#plt.title('Comparing step throughput: TD3 vs. baseline')
#plt.savefig('TD3_0CIO2_{}.png'.format(int(time.time())))




