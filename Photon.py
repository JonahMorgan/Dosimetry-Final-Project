class Particles:
    """Base class for particle types."""
    def __init__(
            self,
            particleType,
            particleStartingPosition,
            particleEnergy, 
            particleDirection
        ):
            self.particleType = particleType
            self.particleStartingPosition = particleStartingPosition
            self.particleEnergy = particleEnergy
            self.particlePathLength = 0
            self.particleDirection = particleDirection


class Photon(Particles):
    def __init__(self, particleStartingPosition, particleEnergy, particleDirection):
        super().__init__("Photon", particleStartingPosition, particleEnergy, particleDirection)

    