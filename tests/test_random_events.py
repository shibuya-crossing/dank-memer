from dank_memer.helper import kraken, dragon


def test_kraken_0():
    assert kraken(kraken_text[0]) == 2


def test_kraken_1():
    assert kraken(kraken_text[1]) == 0


def test_kraken_2():
    assert kraken(kraken_text[2]) == 1


def test_dragon_0():
    assert dragon(dragon_text[0]) == 0


def test_dragon_1():
    assert dragon(dragon_text[1]) == 0


def test_dragon_2():
    assert dragon(dragon_text[2]) == 0


kraken_text = [
    """
Catch the fish!
              <:Kraken:
:bucket::bucket::bucket: 
""",
    """
Catch the fish!
<:legendaryfish:
:bucket::bucket::bucket:
""",
    """
Catch the fish!
       <:legendaryfish:
:bucket::bucket::bucket: 
""",
]

dragon_text = [
    """
Dodge the Fireball
       <:Dragon:
              <:FireBall:
              <:levitate: 
""",
    """
Dodge the Fireball
       <:Dragon:
              <:FireBall:
<:levitate: 
""",
    """
Dodge the Fireball
       <:Dragon:
       <:FireBall:
       <:levitate: 
""",
]
