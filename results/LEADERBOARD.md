# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 412 windows, 11319 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 204 | 35.8 | 36.5 | $-106.95 | -5.2% | $893.05 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 967 | 51.0 | 50.0 | $-210.86 | -2.2% | $789.14 | -0.7 | done | can't tell from luck |
| value_ev10 | 530 | 40.2 | 40.5 | $-221.49 | -4.2% | $778.51 | -0.8 | done | can't tell from luck |
| value_ev5 | 798 | 42.1 | 42.2 | $-310.32 | -3.9% | $689.68 | -1.0 | done | can't tell from luck |
| trend_filter | 644 | 50.2 | 50.7 | $-315.56 | -4.9% | $684.44 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1140 | 49.3 | 49.9 | $-533.83 | -4.7% | $466.17 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1140 | 50.7 | 51.9 | $-715.88 | -6.3% | $284.12 | -2.2 | done | losing for real |
| coinflip | 1643 | 50.3 | 50.9 | $-795.79 | -4.8% | $204.21 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 967 | 49.0 | 51.9 | $-898.50 | -9.3% | $101.50 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1643 | 49.8 | 51.6 | $-1124.18 | -6.8% | $-124.18 | -2.9 | done | losing for real |
| always_up | 1643 | 45.9 | 50.6 | $-2101.04 | -12.8% | $-1101.04 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2561 | 47.8 | 49.5 | $-1773.20 |
| ETH | 2847 | 48.1 | 49.0 | $-1689.48 |
| SOL | 2931 | 47.9 | 49.5 | $-2277.93 |
| XRP | 2980 | 48.8 | 49.3 | $-1593.79 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
