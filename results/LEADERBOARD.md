# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1039 windows, 28851 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 537 | 34.6 | 35.1 | $-294.76 | -5.5% | $705.24 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2931 | 51.2 | 50.5 | $-811.53 | -2.8% | $188.47 | -1.5 | done | can't tell from luck |
| value_ev10 | 1331 | 37.4 | 39.2 | $-1012.06 | -7.6% | $-12.06 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2468 | 49.8 | 49.6 | $-1119.56 | -4.5% | $-119.56 | -2.3 | done | losing for real |
| trend_filter | 1725 | 49.3 | 50.7 | $-1349.42 | -7.8% | $-349.42 | -3.3 | done | losing for real |
| value_ev5 | 2016 | 39.4 | 41.0 | $-1443.93 | -7.2% | $-443.93 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2468 | 50.2 | 51.0 | $-1612.08 | -6.5% | $-612.08 | -3.3 | done | losing for real |
| coinflip | 4148 | 50.5 | 50.3 | $-1681.36 | -4.1% | $-681.36 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2931 | 48.8 | 50.3 | $-2030.85 | -6.9% | $-1030.85 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4148 | 50.7 | 51.5 | $-2295.05 | -5.5% | $-1295.05 | -3.7 | done | losing for real |
| always_up | 4148 | 47.4 | 49.5 | $-3608.12 | -8.7% | $-2608.12 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6577 | 48.3 | 49.0 | $-3636.32 |
| ETH | 7150 | 48.1 | 48.5 | $-4454.78 |
| SOL | 7535 | 48.1 | 48.5 | $-4424.18 |
| XRP | 7589 | 48.1 | 48.3 | $-4743.46 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
