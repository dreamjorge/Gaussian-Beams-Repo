import math
import numpy as np

pi = math.pi

class _k(object):
    """_k magintude of vector of propagation
    :type: float in physical units.
    """
    def __get__(self,obj,owner):
        """__get__ get value of k, with wavelength in object
        :return: value of k with formula.
        :rtype: float in pysical units.
        """        
        k = (2*pi)/(obj.wavelength)
        return k
    def __set__(self,obj,value):
        """__set__ rule for set k value
        :raises TypeError: [description]
        """        
        raise TypeError("k is not possible to set") 

class _RayleighDistance(object):
    """__RayleighDistance  distance of Rayleigh
    :type: float in physical units.
    """
    def __get__(self,obj,owner):
        """__get__ get value of RayleighDistance, with wavelength and initial waist in object
        :return: value of RayleighDistance with formula.
        :rtype: float in pysical units.
        """       
        Rd = (np.square(obj.initialWaist))*(obj.k)/2;  
        return Rd
    def __set__(self,instance,value):
        """__set__ rule for set RayleighDistance value
        :raises TypeError: [description]
        """    
        raise TypeError("Rayleigh Distance is not possible to set") 

class _waist(object):
    def __get__(self,obj,owner):
        """__get__ get value of waist, with zCoordinate and RayleighDistance in object
        :return: value of waist with formula.
        :rtype: float in pysical units.
        """
        waist = (obj.initialWaist)*np.sqrt( np.square(obj.zCoordinate/obj.RayleighDistance) + 1)
        return waist
    def __set__(self,instance,value):
        """__set__ rule for set waist value
        :raises TypeError: [description]
        """    
        raise TypeError("waist is not possible to set") 

class _radius(object):
    def __get__(self,obj,owner):
        """__get__ get value of radius, with zCoordinate and RayleighDistance in object
        :return: value of radius with formula.
        :rtype: float in pysical units.
        """
        if obj.zCoordinate==0 :
            radius = math.inf 
        else:
            radius = (obj.zCoordinate)*(1+np.square(obj.RayleighDistance/obj.zCoordinate));
        return radius

    def __set__(self,instance,value):
        """__set__ rule for set radius value
        :raises TypeError: [description]
        """    
        raise TypeError("radius is not possible to set") 

class _GouyPhase(object):
    def __get__(self,obj,owner):
        """__get__ get value of GouyPhase, with zCoordinate and RayleighDistance in object
        :return: value of GouyPhase with formula.
        :rtype: float in pysical units.
        """
        phi = np.arctan(obj.zCoordinate/obj.RayleighDistance);
        return phi

    def __set__(self,instance,value):
        """__set__ rule for set GouyPhase value
        :raises TypeError: [description]
        """    
        raise TypeError("Gouy phase is not possible to set") 

class _divergenceAngle(object):
    def __get__(self,obj,owner):
        """__get__ get value of divergenceAngle, with zCoordinate and RayleighDistance in object
        :return: value of divergenceAngle with formula.
        :rtype: float in pysical units.
        """
        DivergenceAngle = np.arctan((obj.initialWaist)/(obj.RayleighDistance));
        return DivergenceAngle
    def __set__(self,obj,value):
        """__set__ rule for set divergenceAngle value
        :raises TypeError: [description]
        """    
        raise TypeError("angle of divergence is not possible to set") 

class _amplitude(object):
    def __get__(self,obj,owner):
        """__get__ get value of amplitude, with waist in object
        :return: value of amplitude with formula.
        :rtype: float in pysical units.
        """
        amplitude = 1./obj.waist;
        return amplitude
    def __set__(self,obj,value):
        """__set__ rule for set amplitude value
        :raises TypeError: [description]
        """    
        raise TypeError("amplitude of Gaussian beam is not possible to set") 

class _opticalField(object):
    def __get__(self,obj,owner):
        """__get__ get value of opticalField, all parameters of beam in object
        :return: value of opticalField with formula.
        :rtype: float in pysical units.
        """
        opticalField = obj.amplitude\
                    * np.exp(-np.square(obj.rCoordinate/(obj.waist)))\
                    * np.exp( 1.j*((obj.k)*(np.square(obj.rCoordinate))/(2*(obj.radius))))\
                    * np.exp(-1.j*((obj.GouyPhase)))\
                    * np.exp( 1.j*((obj.k)*(obj.zCoordinate)))#
        return opticalField 
    def __set__(self,obj,value):
        raise TypeError("Optical Field of Gaussian beam is not possible to set") 


class GaussianParameters(object):
    """GaussianParameters 
    This is main object for create a Gaussian Parameters that recives follow inputs:

    zCoordinate:  as distance of propagation.
    initialWaist: initial waist of gaussian beam at zero of distance of propagation.
    wavelength:   wavelength of Gaussian Beam.

    With inputs follow parameters are calculated:

    k:                as magnitude of vector k of light.

    and next are parameters calculated at distance of propagation of Gaussian Beam:

    RayleighDistance:
    waist:            
    radius:
    GouyPhase:
    divergenceAngle:

    :param inputs: recives zCoordinate ,initialWaist ,wavelength as inputs.
    :type inputs:  physical units at floats, zCoordinate can be a vector.
    :return:       object with parameters of Gaussian Beam.
    :rtype:        GaussianParameters as object.
    """    
    
    #Classes of parameters with dependences
    k                = _k()
    RayleighDistance = _RayleighDistance()
    waist            = _waist()
    radius           = _radius()
    GouyPhase        = _GouyPhase()
    divergenceAngle  = _divergenceAngle()

    #constructor with input variables as show in follow line
    def __init__(self ,zCoordinate ,initialWaist ,wavelength):
        
        self.zCoordinate      = zCoordinate
        self.initialWaist     = initialWaist
        self.wavelength       = wavelength


class GuassianBeam(GaussianParameters):
    """GuassianBeam
    This is main  object of Gaussian Beams that recives follow variables as inputs:
    rCoordinate:  radial coordinate of Gaussian Beam, this can be used in 1 or 2 dimentions.
    zCoordinate:  distance of propagation of Gaussian Beam.
    initialWaist: initial waist of gaussian beam at zero of distance of propagation.
    wavelength:   wavelength of Gaussian Beam.

    :param: GaussianParameters: rCoordinate ,zCoordinate , initialWaist, wavelength as inputs.
    :type inputs: physical units at flaots, rCoordinate ,zCoordinate can be vectors.
    :return:      object of Optical Field of Gaussian Beam and their parameters.
    :rtype:       GaussianBeam as object
    """
    #Classes of parameters with dependences
    amplitude    = _amplitude()
    opticalField = _opticalField()

    #constructor of Gaussian Beam
    def __init__(self ,rCoordinate ,zCoordinate , initialWaist, wavelength):
        #calling GaussianParameters object with inputs, for create object.
        super().__init__( zCoordinate, initialWaist , wavelength)

        self.rCoordinate = rCoordinate
