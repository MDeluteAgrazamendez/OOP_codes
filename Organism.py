from abc import ABC, abstractmethod

class Organism(ABC):
    """An abstract base class representing a genetic
    organism.

    This class serves as a blueprint for specific organism
    types (e.g., Bacteria, Viruses). It encapsulates the
    organism's species name and genomic sequence, providing
    secure validation interfaces for genetic data.

    Attributes:
        species (str): The common or scientific name of the
        organism species.
    """

    def __init__(self, species, sequence):
        """Initializes the Organism with a species name and
        a standardized sequence.

        Args:
            species (str): The name of the organism species.
            sequence (str): The initial genetic sequence
                (DNA/RNA). It will automatically be
                converted to uppercase.
        """
        self.species = species
        # Encapsulation: Hidden attribute
        self.__sequence = sequence.upper() 
    
    def get_sequence(self):
        """Retrieves the hidden genetic sequence.

        Returns:
            str: The uppercase genetic sequence string.
        """
        return self.__sequence
    
    def set_sequence(self, new_sequence):
        """Validates and updates the hidden genetic
        sequence.

        The sequence will only be updated if it meets the
        structural criteria:
        minimum length requirements, containing the start
        codon, and consisting only of valid genomic bases
        (A, T, C, G).

        Args:
            new_sequence (str): The raw candidate genetic
            sequence string to evaluate.

        Returns:
            None
        """
        cleaned = new_sequence.upper()
        if (len(cleaned) >= MIN_LENGTH and 
            START_CODON in cleaned and 
            set(cleaned).issubset(VALID_BASES)):
            self.__sequence = cleaned
            print(f"[{self.species}] Sequence updated successfully!")
        else:
            print(f"[{self.species}] Error: Invalid sequence. Rejected!")

    def transcribe(self):
        """Transcribes the internal DNA sequence into an RNA
        sequence.

        Replaces all Thymine ('T') bases with Uracil ('U').

        Returns:
            str: The transcribed RNA sequence string.
        """
        return self.__sequence.replace("T", "U")

    @abstractmethod
    def reproduce(self):
        """Abstract method that defines how the organism
        reproduces.

        Must be overridden by all concrete child subclasses.

        Raises:
            TypeError: If a child class fails to implement
            this method.
        """
        pass

# Child Class 1: Bacteria
class Bacteria(Organism):
    """Represents a bacterial organism inheriting basic
    traits from Organism.

    Bacteria are single-celled organisms that implement a
    specific, asexual method of reproduction.
    """

    def reproduce(self):
        """Simulates bacterial reproduction via binary
        fission.

        Returns:
            str: A descriptive message detailing the cloning
                process.
        """
        return f"{self.species} splits via binary fission to clone itself!"


# Child Class 2: Virus
class Virus(Organism):
    """Represents a viral organism inheriting basic traits
    from Organism.

    Viruses are non-cellular entities that require a host
    organism to replicate and can actively infect other
    organisms.

    Attributes:
        virus_type (str): The genetic classification of the
            virus (e.g., 'DNA' or 'RNA').
    """

    def __init__(self, species, sequence, virus_type = "DNA"):
        """Initializes the Virus with common organism
        traits and a specific type.

        Args:
            species (str): The name of the virus species.
            sequence (str): The genetic sequence string.
            virus_type (str): The genetic material
                classification (e.g., "DNA", "RNA").
        """
        # Inheritance: Calling the parent constructor
        super().__init__(species, sequence)
        self.virus_type = virus_type  # Unique attribute
        
    def reproduce(self):
        """Simulates viral replication within an ecosystem.

        Returns:
            str: A descriptive message detailing host cell
                hijacking.
        """
        return f"{self.species} replicates by hijacking a host cell!"
    
    def infect(self, host_organism):
        """Simulates the virus infecting another target
        organism.

        Args:
            host_organism (Organism): An instance of an
                Organism subclass that the virus is
                attempting to infect.

        Returns:
            str: A message documenting the successful
            infection event.
        """
        return f"{self.species} ({self.virus_type}) has infected a {host_organism.species}!"

# Multiple Inheritance: inheriting from both Bacteria and Virus
class SyntheticMicrobe(Bacteria, Virus):
    """A hybrid, laboratory-created entity combining traits
    of Bacteria and Virus.

    Through multiple inheritance, this class possesses the
    genetic structure and binary fission reproduction
    capabilities of Bacteria, alongside the host-infecting
    capabilities of a Virus.

    Method Resolution Order (MRO) Quirks:
        Because Bacteria is listed before Virus in the class
        definition, Python's lookup chain resolves shared
        methods (like reproduce()) using the Bacteria
        implementation first. 
        
        The resolution path is: 
        SyntheticMicrobe -> Bacteria -> Virus -> Organism
            -> ABC -> object
    """
    pass

# --- Simulation Testing ---
if __name__ == "__main__":
    # 01 Instantiate objects
    sol_bacteria = Bacteria("Solar Bacteria", "ATGCTAGTC")
    neb_virus = Virus("Nebula Virus", "ATGCGATAA", "RNA")

    # 02 Polymorphism List
    planet_ecosystem = [sol_bacteria, neb_virus]

    # 03 Dynamic Loop
    print("--- Ecosystem Reproduction Simulation ---")
    for organism in planet_ecosystem:
        print(organism.reproduce())
        
    print("\n--- Interaction Simulation ---")
    print(neb_virus.infect(sol_bacteria))

    # 04 Make a hybrid microbe!
    cyborg_bug = SyntheticMicrobe("X-1", "ATGCTAGTC")
    print(cyborg_bug.reproduce())