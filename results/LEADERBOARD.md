# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 10:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 114 windows, 2923 settled trades, 41 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 223 | 61.0 | 53.0 | $+287.46 | +12.9% | $1287.46 | +2.0 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 282 | 56.0 | 52.0 | $+161.12 | +5.7% | $1161.12 | +1.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 449 | 52.1 | 50.6 | $-33.43 | -0.7% | $966.57 | -0.2 | done | can't tell from luck |
| value_ev10 | 149 | 40.9 | 40.7 | $-57.82 | -3.9% | $942.18 | -0.4 | Thu 8:45 AM | too few trades (149/200) |
| value_ev20 | 51 | 29.4 | 36.6 | $-111.54 | -21.9% | $888.46 | -1.3 | Sun 4:00 PM | too few trades (51/200) |
| coinflip | 449 | 50.8 | 51.3 | $-214.87 | -4.8% | $785.13 | -1.1 | done | can't tell from luck |
| value_ev5 | 212 | 39.2 | 42.2 | $-228.75 | -10.8% | $771.25 | -1.4 | done | can't tell from luck |
| trend_filter | 154 | 40.9 | 48.8 | $-287.88 | -18.7% | $712.12 | -2.3 | Thu 7:15 AM | too few trades (154/200) |
| momentum_15m_0.10pct | 282 | 44.0 | 50.1 | $-419.39 | -14.9% | $580.61 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 223 | 39.0 | 49.1 | $-499.37 | -22.4% | $500.63 | -3.4 | done | losing for real |
| always_up | 449 | 46.3 | 50.4 | $-518.90 | -11.6% | $481.10 | -2.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 634 | 46.1 | 49.8 | $-555.73 |
| ETH | 713 | 46.0 | 49.0 | $-626.83 |
| SOL | 779 | 48.3 | 48.6 | $-519.31 |
| XRP | 797 | 50.3 | 49.1 | $-221.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
