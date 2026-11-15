# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 378 windows, 10292 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 8:45 PM | too few trades (196/200) |
| value_ev10 | 500 | 40.0 | 40.4 | $-209.12 | -4.2% | $790.88 | -0.8 | done | can't tell from luck |
| value_ev5 | 738 | 41.6 | 42.1 | $-342.45 | -4.6% | $657.55 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 858 | 49.8 | 49.7 | $-366.52 | -4.3% | $633.48 | -1.3 | done | can't tell from luck |
| trend_filter | 570 | 48.8 | 50.4 | $-442.00 | -7.8% | $558.00 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1027 | 51.5 | 52.2 | $-541.77 | -5.3% | $458.23 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1027 | 48.5 | 49.6 | $-597.96 | -5.8% | $402.04 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 858 | 50.2 | 52.1 | $-636.79 | -7.4% | $363.21 | -2.3 | done | losing for real |
| coinflip | 1506 | 49.8 | 50.8 | $-846.15 | -5.6% | $153.85 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1506 | 49.5 | 51.5 | $-1109.49 | -7.4% | $-109.49 | -3.0 | done | losing for real |
| always_up | 1506 | 45.9 | 50.8 | $-1963.02 | -13.0% | $-963.02 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2322 | 47.4 | 49.4 | $-1792.70 |
| ETH | 2593 | 47.6 | 48.9 | $-1886.23 |
| SOL | 2662 | 47.9 | 49.4 | $-1993.55 |
| XRP | 2715 | 48.7 | 49.1 | $-1409.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
