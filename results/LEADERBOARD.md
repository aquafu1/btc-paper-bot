# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 6:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 148 windows, 3742 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 261 | 60.2 | 53.0 | $+286.73 | +11.0% | $1286.73 | +1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 360 | 56.1 | 52.2 | $+176.07 | +4.9% | $1176.07 | +1.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 585 | 53.0 | 51.4 | $-65.44 | -1.1% | $934.56 | -0.3 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 1:30 AM | too few trades (74/200) |
| coinflip | 585 | 51.5 | 51.0 | $-218.14 | -3.7% | $781.86 | -0.9 | done | can't tell from luck |
| value_ev10 | 196 | 37.2 | 40.7 | $-262.43 | -13.4% | $737.57 | -1.6 | Thu 7:30 AM | too few trades (196/200) |
| trend_filter | 189 | 42.3 | 49.3 | $-327.78 | -17.3% | $672.22 | -2.4 | Thu 9:00 AM | too few trades (189/200) |
| value_ev5 | 286 | 38.5 | 42.3 | $-389.73 | -13.6% | $610.27 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 360 | 43.9 | 50.1 | $-550.91 | -15.3% | $449.09 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 261 | 39.8 | 49.3 | $-561.82 | -21.5% | $438.18 | -3.5 | done | losing for real |
| always_up | 585 | 46.2 | 49.9 | $-707.15 | -12.1% | $292.85 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 807 | 45.8 | 49.6 | $-831.58 |
| ETH | 923 | 45.6 | 48.8 | $-986.44 |
| SOL | 982 | 48.6 | 48.8 | $-672.88 |
| XRP | 1030 | 50.6 | 49.1 | $-273.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
