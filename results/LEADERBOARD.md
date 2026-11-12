# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 4:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 141 windows, 3535 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 245 | 61.6 | 53.1 | $+333.39 | +13.6% | $1333.39 | +2.3 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 339 | 57.2 | 52.2 | $+248.23 | +7.3% | $1248.23 | +1.4 | done | can't tell from luck |
| value_ev20 | 67 | 31.3 | 37.0 | $-135.47 | -20.2% | $864.53 | -1.4 | Sun 6:30 AM | too few trades (67/200) |
| momentum_5m_0.00pct | 556 | 52.0 | 51.2 | $-145.50 | -2.6% | $854.50 | -0.6 | done | can't tell from luck |
| coinflip | 556 | 51.6 | 51.0 | $-185.21 | -3.3% | $814.79 | -0.8 | done | can't tell from luck |
| value_ev10 | 185 | 37.3 | 40.7 | $-235.28 | -12.7% | $764.72 | -1.5 | Thu 7:45 AM | too few trades (185/200) |
| value_ev5 | 269 | 38.3 | 42.3 | $-364.16 | -13.5% | $635.84 | -2.0 | done | can't tell from luck |
| trend_filter | 178 | 40.4 | 49.2 | $-368.37 | -20.7% | $631.63 | -2.8 | Thu 9:15 AM | too few trades (178/200) |
| always_up | 556 | 47.7 | 50.2 | $-519.64 | -9.3% | $480.36 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 339 | 42.8 | 50.1 | $-587.03 | -17.3% | $412.97 | -3.2 | done | losing for real |
| momentum_60m_0.30pct | 245 | 38.4 | 49.2 | $-595.20 | -24.3% | $404.80 | -3.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 757 | 45.7 | 49.6 | $-793.89 |
| ETH | 874 | 45.1 | 48.8 | $-1008.43 |
| SOL | 932 | 48.8 | 48.8 | $-572.64 |
| XRP | 972 | 50.9 | 49.2 | $-179.29 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
