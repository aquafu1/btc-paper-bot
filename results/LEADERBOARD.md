# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 7:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 959 windows, 26582 settled trades, 26 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 488 | 35.2 | 34.9 | $-139.50 | -2.9% | $860.50 | -0.5 | done | can't tell from luck |
| value_ev10 | 1207 | 38.3 | 39.1 | $-624.27 | -5.2% | $375.73 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2716 | 51.4 | 50.6 | $-689.88 | -2.5% | $310.12 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2269 | 50.1 | 49.7 | $-891.20 | -3.9% | $108.80 | -1.9 | done | can't tell from luck |
| value_ev5 | 1834 | 40.1 | 41.0 | $-975.09 | -5.3% | $24.91 | -1.9 | done | can't tell from luck |
| trend_filter | 1590 | 49.9 | 50.9 | $-1065.59 | -6.7% | $-65.59 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2269 | 49.9 | 51.0 | $-1600.05 | -7.1% | $-600.05 | -3.4 | done | losing for real |
| coinflip | 3831 | 50.1 | 50.4 | $-1804.24 | -4.7% | $-804.24 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2716 | 48.6 | 50.3 | $-1937.84 | -7.1% | $-937.84 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 3831 | 50.8 | 51.5 | $-2026.61 | -5.3% | $-1026.61 | -3.4 | done | losing for real |
| always_up | 3831 | 46.9 | 49.6 | $-3771.30 | -9.8% | $-2771.30 | -6.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6059 | 48.1 | 49.0 | $-3482.10 |
| ETH | 6604 | 48.1 | 48.5 | $-4008.73 |
| SOL | 6934 | 48.2 | 48.6 | $-3835.98 |
| XRP | 6985 | 48.2 | 48.5 | $-4198.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
