#!/usr/bin/python3

import math
import physical_constants as phys_cons



def compton_wavelength(mass):
	"""returns the Compton wavelength of a particle when given a mass in kg"""
	return phys_cons.h / (phys_cons.c * mass)

def deg_to_rad(angle):
	"""converts an angle in degrees to radians"""
	return (angle * math.pi / 180.0e0)

def rad_to_deg(angle):
	"""converts an angle in radians to degrees"""
	return (angle * 180.0e0 / math.pi)

def compton_scatter(mass, angle, is_degrees = False):
	if is_degrees == False:
		return compton_wavelength(mass) * (1 - math.cos(angle))
	else:
		return compton_wavelength(mass) * (1 - math.cos(deg_to_rad(angle)))

if __name__ == '__main__':
	print ('photons scattering off an electron experience the following wavelength shifts at the listed angles:')
	print ('15 degrees : %e meters' % compton_scatter(phys_cons.m_e, 15, 'True') )
	print ('30 degrees : %e meters' % compton_scatter(phys_cons.m_e, 30, 'True') )
	print ('45 degrees : %e meters' % compton_scatter(phys_cons.m_e, 45, 'True') )
	print ('60 degrees : %e meters' % compton_scatter(phys_cons.m_e, 60, 'True') )
	print ('75 degrees : %e meters' % compton_scatter(phys_cons.m_e, 75, 'True') )
	print ('90 degrees : %e meters' % compton_scatter(phys_cons.m_e, 90, 'True') )
	print ('180 degrees: %e meters' % compton_scatter(phys_cons.m_e, 180, 'True') )
	print ('pi/2 rads  : %e meters' % compton_scatter(phys_cons.m_e, math.pi / 2) )
	print ('pi rads    : %e meters' % compton_scatter(phys_cons.m_e, math.pi) )
