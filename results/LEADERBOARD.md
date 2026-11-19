# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 7:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 766 windows, 21124 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 397 | 33.5 | 34.9 | $-321.45 | -8.1% | $678.55 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2158 | 51.4 | 50.6 | $-541.01 | -2.5% | $458.99 | -1.2 | done | can't tell from luck |
| value_ev10 | 966 | 37.9 | 39.1 | $-641.05 | -6.6% | $358.95 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1785 | 49.9 | 49.5 | $-702.11 | -3.9% | $297.89 | -1.7 | done | can't tell from luck |
| trend_filter | 1242 | 49.8 | 50.8 | $-805.43 | -6.5% | $194.57 | -2.3 | done | losing for real |
| value_ev5 | 1459 | 40.2 | 41.0 | $-847.45 | -5.8% | $152.55 | -1.9 | done | can't tell from luck |
| coinflip | 3058 | 50.4 | 50.2 | $-1182.49 | -3.9% | $-182.49 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1785 | 50.1 | 51.3 | $-1239.78 | -6.9% | $-239.78 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2158 | 48.6 | 50.2 | $-1550.39 | -7.2% | $-550.39 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3058 | 50.9 | 51.7 | $-1559.19 | -5.1% | $-559.19 | -2.9 | done | losing for real |
| always_up | 3058 | 47.1 | 49.6 | $-2841.21 | -9.3% | $-1841.21 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4794 | 48.2 | 49.1 | $-2909.17 |
| ETH | 5278 | 48.0 | 48.5 | $-3508.67 |
| SOL | 5493 | 48.1 | 48.6 | $-3217.18 |
| XRP | 5559 | 48.6 | 48.5 | $-2596.55 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
