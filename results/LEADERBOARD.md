# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 778 windows, 21463 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1816 | 50.1 | 49.6 | $-702.75 | -3.9% | $297.25 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2192 | 51.0 | 50.6 | $-735.22 | -3.4% | $264.78 | -1.6 | done | can't tell from luck |
| trend_filter | 1266 | 50.2 | 50.8 | $-742.42 | -5.9% | $257.58 | -2.1 | done | losing for real |
| value_ev10 | 981 | 37.4 | 39.1 | $-764.62 | -7.8% | $235.38 | -2.0 | done | can't tell from luck |
| value_ev5 | 1484 | 39.8 | 41.0 | $-995.88 | -6.7% | $4.12 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1816 | 49.9 | 51.2 | $-1269.11 | -7.0% | $-269.11 | -3.0 | done | losing for real |
| coinflip | 3104 | 50.2 | 50.3 | $-1353.67 | -4.4% | $-353.67 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2192 | 49.0 | 50.2 | $-1392.93 | -6.4% | $-392.93 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3104 | 51.2 | 51.6 | $-1409.15 | -4.5% | $-409.15 | -2.6 | done | losing for real |
| always_up | 3104 | 47.2 | 49.5 | $-2764.49 | -8.9% | $-1764.49 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4875 | 48.2 | 49.1 | $-2909.14 |
| ETH | 5359 | 48.0 | 48.5 | $-3562.32 |
| SOL | 5587 | 48.1 | 48.6 | $-3272.40 |
| XRP | 5642 | 48.5 | 48.5 | $-2777.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
