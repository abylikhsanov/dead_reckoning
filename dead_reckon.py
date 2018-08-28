import numpy as np

def calc_lin_vel_and_theta(l,w_l, w_r, r):
	b = np.matrix([[1,1],[1/l, -1/l]], np.float32)
	c = np.matrix([[w_r], [w_l]], np.float32)
	a = (r/2)*b*c
	return a

def dead_reckon(T,w_l, w_r,l,r,theta, posx, posy):
	theta_T = 0.0
	posx_T = 0.0
	posy_T = 0.0
	s = 0.0
	if w_l == w_r:
		v = calc_lin_vel_and_theta(l,w_l,w_r,r)[0]
		s = v*T
		theta_T = theta
		posx_T = posx + (s*np.cos(theta_T))
		posy_T = posy + (s*np.sin(theta_T))

	elif abs(w_l) == abs(w_r):
		angular = calc_lin_vel_and_theta(l,w_l,w_r,r)[1]
		theta_diff = angular*T
		theta_T = theta+theta_diff
		posx_T = posx
		posy_T = posy