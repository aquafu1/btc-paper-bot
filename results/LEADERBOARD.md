# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1129 windows, 31195 settled trades, 39 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 595 | 34.6 | 35.2 | $-355.99 | -6.0% | $644.01 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3141 | 51.2 | 50.5 | $-824.07 | -2.6% | $175.93 | -1.5 | done | can't tell from luck |
| value_ev10 | 1458 | 38.2 | 39.2 | $-875.40 | -6.0% | $124.60 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2636 | 49.7 | 49.4 | $-1128.41 | -4.3% | $-128.41 | -2.2 | done | losing for real |
| value_ev5 | 2209 | 40.1 | 41.1 | $-1277.18 | -5.8% | $-277.18 | -2.3 | done | losing for real |
| trend_filter | 1849 | 49.1 | 50.4 | $-1438.45 | -7.8% | $-438.45 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2636 | 50.3 | 51.1 | $-1656.26 | -6.3% | $-656.26 | -3.3 | done | losing for real |
| coinflip | 4510 | 50.4 | 50.2 | $-1781.16 | -3.9% | $-781.16 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 3141 | 48.8 | 50.2 | $-2092.71 | -6.7% | $-1092.71 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4510 | 50.3 | 51.4 | $-2739.80 | -6.1% | $-1739.80 | -4.2 | done | losing for real |
| always_up | 4510 | 47.7 | 49.4 | $-3466.57 | -7.7% | $-2466.57 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7152 | 48.3 | 49.0 | $-3656.84 |
| ETH | 7728 | 48.1 | 48.4 | $-4647.96 |
| SOL | 8117 | 48.0 | 48.4 | $-4597.86 |
| XRP | 8198 | 48.2 | 48.2 | $-4733.35 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
