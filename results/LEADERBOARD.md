# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 12:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 736 windows, 20310 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 383 | 33.4 | 34.9 | $-332.66 | -8.7% | $667.34 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2083 | 51.6 | 50.7 | $-476.84 | -2.3% | $523.16 | -1.0 | done | can't tell from luck |
| value_ev10 | 928 | 37.9 | 39.1 | $-626.66 | -6.8% | $373.34 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1710 | 49.9 | 49.5 | $-656.90 | -3.8% | $343.10 | -1.6 | done | can't tell from luck |
| value_ev5 | 1400 | 40.4 | 41.1 | $-761.72 | -5.4% | $238.28 | -1.7 | done | can't tell from luck |
| trend_filter | 1193 | 49.9 | 50.9 | $-770.04 | -6.5% | $229.96 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1710 | 50.1 | 51.3 | $-1169.48 | -6.8% | $-169.48 | -2.9 | done | losing for real |
| coinflip | 2940 | 50.3 | 50.3 | $-1175.32 | -4.0% | $-175.32 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2083 | 48.4 | 50.1 | $-1503.20 | -7.2% | $-503.20 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2940 | 50.9 | 51.8 | $-1601.89 | -5.4% | $-601.89 | -3.1 | done | losing for real |
| always_up | 2940 | 47.0 | 49.6 | $-2729.07 | -9.3% | $-1729.07 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4602 | 48.1 | 49.1 | $-2919.18 |
| ETH | 5062 | 48.1 | 48.6 | $-3152.21 |
| SOL | 5288 | 48.1 | 48.7 | $-3083.49 |
| XRP | 5358 | 48.5 | 48.5 | $-2648.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
