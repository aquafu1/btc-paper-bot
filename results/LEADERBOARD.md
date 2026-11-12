# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 4:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 141 windows, 3543 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 245 | 61.6 | 53.1 | $+333.39 | +13.6% | $1333.39 | +2.3 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 340 | 57.4 | 52.2 | $+252.77 | +7.4% | $1252.77 | +1.4 | done | can't tell from luck |
| momentum_5m_0.00pct | 557 | 52.1 | 51.2 | $-140.96 | -2.5% | $859.04 | -0.6 | done | can't tell from luck |
| value_ev20 | 68 | 30.9 | 37.0 | $-145.47 | -21.4% | $854.53 | -1.5 | Sun 5:45 AM | too few trades (68/200) |
| coinflip | 557 | 51.5 | 51.0 | $-195.21 | -3.5% | $804.79 | -0.9 | done | can't tell from luck |
| value_ev10 | 186 | 37.1 | 40.7 | $-245.28 | -13.2% | $754.72 | -1.6 | Thu 7:45 AM | too few trades (186/200) |
| trend_filter | 178 | 40.4 | 49.2 | $-368.37 | -20.7% | $631.63 | -2.8 | Thu 9:30 AM | too few trades (178/200) |
| value_ev5 | 270 | 38.1 | 42.3 | $-374.16 | -13.9% | $625.84 | -2.0 | done | losing for real |
| always_up | 557 | 47.6 | 50.2 | $-529.64 | -9.5% | $470.36 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 245 | 38.4 | 49.2 | $-595.20 | -24.3% | $404.80 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 340 | 42.6 | 50.1 | $-597.03 | -17.6% | $402.97 | -3.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 765 | 45.5 | 49.5 | $-844.81 |
| ETH | 874 | 45.1 | 48.8 | $-1008.43 |
| SOL | 932 | 48.8 | 48.8 | $-572.64 |
| XRP | 972 | 50.9 | 49.2 | $-179.29 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
