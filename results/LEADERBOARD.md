# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 11:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1548 windows, 38055 settled trades, 402 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 783 | 34.1 | 35.3 | $-663.27 | -8.5% | $336.73 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3772 | 50.9 | 50.0 | $-992.28 | -2.6% | $7.72 | -1.6 | done | can't tell from luck |
| value_ev10 | 1872 | 38.4 | 39.1 | $-1073.92 | -5.7% | $-73.92 | -2.0 | done | losing for real |
| value_ev5 | 2817 | 40.4 | 41.1 | $-1477.57 | -5.2% | $-477.57 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 3167 | 51.0 | 51.0 | $-1542.30 | -4.9% | $-542.30 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 3167 | 49.0 | 49.2 | $-1659.28 | -5.2% | $-659.28 | -2.9 | done | losing for real |
| trend_filter | 2247 | 48.6 | 50.3 | $-1931.41 | -8.6% | $-931.41 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3772 | 49.1 | 50.2 | $-2345.64 | -6.2% | $-1345.64 | -3.8 | done | losing for real |
| coinflip | 5486 | 49.9 | 49.9 | $-2437.58 | -4.4% | $-1437.58 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5486 | 50.1 | 51.3 | $-3437.57 | -6.3% | $-2437.57 | -4.8 | done | losing for real |
| always_up | 5486 | 48.1 | 49.2 | $-3566.76 | -6.5% | $-2566.76 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9988 | 47.9 | 48.7 | $-5764.94 |
| ETH | 10757 | 48.0 | 47.8 | $-5778.40 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
