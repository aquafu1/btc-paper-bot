# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 8:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 963 windows, 26673 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 492 | 35.0 | 34.9 | $-179.50 | -3.6% | $820.50 | -0.6 | done | can't tell from luck |
| value_ev10 | 1216 | 38.2 | 39.1 | $-659.76 | -5.4% | $340.24 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 2724 | 51.4 | 50.5 | $-689.02 | -2.5% | $310.98 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 2271 | 50.1 | 49.7 | $-911.20 | -4.0% | $88.80 | -1.9 | done | can't tell from luck |
| value_ev5 | 1844 | 40.0 | 41.0 | $-1020.59 | -5.5% | $-20.59 | -2.0 | done | can't tell from luck |
| trend_filter | 1593 | 49.9 | 50.9 | $-1063.19 | -6.7% | $-63.19 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2271 | 49.9 | 51.0 | $-1565.55 | -6.9% | $-565.55 | -3.4 | done | losing for real |
| coinflip | 3846 | 50.2 | 50.4 | $-1775.51 | -4.6% | $-775.51 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 3846 | 50.9 | 51.6 | $-1950.40 | -5.1% | $-950.40 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2724 | 48.6 | 50.3 | $-1955.29 | -7.2% | $-955.29 | -3.8 | done | losing for real |
| always_up | 3846 | 46.9 | 49.6 | $-3731.44 | -9.7% | $-2731.44 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6079 | 48.1 | 49.0 | $-3506.92 |
| ETH | 6623 | 48.1 | 48.5 | $-4066.75 |
| SOL | 6972 | 48.3 | 48.6 | $-3748.76 |
| XRP | 6999 | 48.2 | 48.5 | $-4179.02 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
