# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 1:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 128 windows, 3231 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 234 | 62.0 | 53.1 | $+336.30 | +14.4% | $1336.30 | +2.4 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 305 | 56.4 | 52.0 | $+184.62 | +6.1% | $1184.62 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 504 | 52.8 | 50.9 | $-39.04 | -0.8% | $960.96 | -0.2 | done | can't tell from luck |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 6:45 AM | too few trades (61/200) |
| value_ev10 | 170 | 37.1 | 40.3 | $-214.30 | -12.6% | $785.70 | -1.4 | Thu 7:15 AM | too few trades (170/200) |
| coinflip | 504 | 50.8 | 51.1 | $-265.80 | -5.3% | $734.20 | -1.2 | done | can't tell from luck |
| trend_filter | 168 | 41.1 | 48.9 | $-321.43 | -19.1% | $678.57 | -2.5 | Thu 7:45 AM | too few trades (168/200) |
| value_ev5 | 242 | 36.8 | 41.9 | $-389.45 | -16.1% | $610.55 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 305 | 43.6 | 50.2 | $-486.58 | -16.0% | $513.42 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 234 | 38.0 | 49.1 | $-577.49 | -24.7% | $422.51 | -3.8 | done | losing for real |
| always_up | 504 | 46.0 | 50.3 | $-653.27 | -13.0% | $346.73 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 695 | 45.2 | 49.5 | $-795.66 |
| ETH | 796 | 44.8 | 48.7 | $-946.98 |
| SOL | 856 | 48.6 | 48.6 | $-553.42 |
| XRP | 884 | 50.1 | 49.0 | $-313.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
