# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 2:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 131 windows, 3301 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 235 | 62.1 | 53.1 | $+342.92 | +14.6% | $1342.92 | +2.4 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 315 | 56.8 | 52.2 | $+204.95 | +6.5% | $1204.95 | +1.2 | done | can't tell from luck |
| momentum_5m_0.00pct | 516 | 52.1 | 50.9 | $-100.57 | -1.9% | $899.43 | -0.5 | done | can't tell from luck |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 9:15 AM | too few trades (61/200) |
| coinflip | 516 | 51.4 | 51.1 | $-216.23 | -4.2% | $783.77 | -1.0 | done | can't tell from luck |
| value_ev10 | 174 | 36.8 | 40.5 | $-232.46 | -13.4% | $767.54 | -1.5 | Thu 7:15 AM | too few trades (174/200) |
| trend_filter | 169 | 40.8 | 48.9 | $-331.43 | -19.6% | $668.57 | -2.5 | Thu 8:30 AM | too few trades (169/200) |
| value_ev5 | 249 | 36.9 | 42.0 | $-394.45 | -15.8% | $605.55 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 315 | 43.2 | 50.0 | $-521.26 | -16.5% | $478.74 | -3.0 | done | losing for real |
| momentum_60m_0.30pct | 235 | 37.9 | 49.1 | $-587.49 | -25.0% | $412.51 | -3.9 | done | losing for real |
| always_up | 516 | 46.5 | 50.3 | $-617.75 | -12.0% | $382.25 | -2.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 707 | 45.1 | 49.5 | $-820.19 |
| ETH | 815 | 45.0 | 48.7 | $-931.80 |
| SOL | 875 | 48.6 | 48.6 | $-569.16 |
| XRP | 904 | 50.2 | 49.1 | $-315.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
