"""Classes de domínio dos imóveis disponíveis para locação."""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Imovel(ABC):
    """Classe-base: define o comportamento comum a todos os imóveis."""

    @abstractmethod
    def calcular_aluguel(self) -> float:
        """Retorna o valor mensal do aluguel, sem o contrato imobiliário."""


@dataclass(frozen=True)
class Apartamento(Imovel):
    quartos: int = 1
    com_garagem: bool = False
    possui_criancas: bool = True

    def __post_init__(self) -> None:
        if self.quartos not in (1, 2):
            raise ValueError("O apartamento deve ter 1 ou 2 quartos.")

    def calcular_aluguel(self) -> float:
        valor = 700.0
        if self.quartos == 2:
            valor += 200.0
        if self.com_garagem:
            valor += 300.0
        if not self.possui_criancas:
            valor *= 0.95
        return round(valor, 2)


@dataclass(frozen=True)
class Casa(Imovel):
    quartos: int = 1
    com_garagem: bool = False

    def __post_init__(self) -> None:
        if self.quartos not in (1, 2):
            raise ValueError("A casa deve ter 1 ou 2 quartos.")

    def calcular_aluguel(self) -> float:
        valor = 900.0
        if self.quartos == 2:
            valor += 250.0
        if self.com_garagem:
            valor += 300.0
        return valor


@dataclass(frozen=True)
class Estudio(Imovel):
    vagas: int = 0

    def __post_init__(self) -> None:
        if self.vagas == 1 or self.vagas < 0:
            raise ValueError("O estúdio permite 0 ou a partir de 2 vagas.")

    def calcular_aluguel(self) -> float:
        valor = 1200.0
        if self.vagas >= 2:
            valor += 250.0 + (self.vagas - 2) * 60.0
        return valor
