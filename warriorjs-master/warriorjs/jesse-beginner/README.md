## Jesse - beginner - level 3

### _The air feels thicker than before. There must be a horde of sludge._

> **TIP:** Be careful not to die! Use `warrior.health()` to keep an eye on your health, and `warrior.rest()` to earn 10% of your max health back.


### Floor Map

```
╔═════════╗
║@ s ss s>║
╚═════════╝

@ = Jesse (20 HP)
s = Sludge (12 HP)
> = stairs
```

### Abilities

#### Actions (only one per turn)

* `warrior.rest()`: Gain 10% of max health back, but do nothing more.
* `warrior.walk()`: Move one space in the given direction (forward by default).
* `warrior.attack()`: Attack a unit in the given direction (forward by default) dealing 5 HP of damage.

#### Senses

* `warrior.health()`: Return an integer representing your health.
* `warrior.think()`: Think about your options before choosing an action.
* `warrior.feel()`: Return the adjacent space in the given direction (forward by default).

### Next Steps

When you're done editing `Player.js`, run the `warriorjs` command again.
