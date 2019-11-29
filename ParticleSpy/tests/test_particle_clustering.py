from ParticleSpy import api as ps
import hyperspy.api as hs
import os

def test_clustering():
    my_path = os.path.dirname(__file__)
    
    data = hs.load(os.path.join(os.path.par_dir(my_path), 'Data/SiO2 HAADF Image.hspy'))
    
    params = ps.parameters()
    params.generate(threshold='otsu',watershed=True,min_size=5,rb_kernel=100)
    
    particles = ps.ParticleAnalysis(data,params)
    
    new_plists = particles.cluster_particles(properties=['area','circularity'])
    
    assert len(new_plists[0].list) == 43 or len(new_plists[0].list) == 59