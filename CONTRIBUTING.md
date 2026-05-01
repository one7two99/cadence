# Contributing to Cadence

All contributions welcome — from a typo fix to a full ZMK port.

## Report a problem
Open an **Issue** using the Bug Report template. Include keyboard hardware
revision, firmware version, which key/layer misbehaves, and steps to reproduce.

## Suggest an improvement
Open a **Discussion** to explore ideas, or an **Issue** with the Feature
Request template for concrete proposals.

## Submit a change
1. Fork the repository
2. Branch: `git checkout -b feat/your-feature`
3. Commit clearly: `git commit -m "feat: add ZMK port"`
4. Open a Pull Request against `main`

## Port to another keyboard or firmware
Cadence is the Sweep adaptation of Cadenza. Further ports — for example to
ZMK firmware, to other 34-key boards, or to Choc-spaced variants — are
welcome. Place files in `firmware/ports/<keyboard>/`, include a README
documenting differences, then open a Discussion to announce it.

## Cross-family consistency
Cadence is part of a layout family (Cadenza, Cadence, Sonata, Coda). When
proposing changes, please consider the impact on muscle-memory consistency
with sibling projects. Changes that diverge from Cadenza's shared positions
(Bottom Row layer access, Home Row HRMs, Frequency+Strength symbols, Path
TD, Bracket pairs) need a stronger justification than Cadence-internal
optimisations.

## Attribution
All contributors listed in CONTRIBUTORS.md once the first external
contribution arrives.
