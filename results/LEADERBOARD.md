# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 604 windows, 16684 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 326 | 34.4 | 35.2 | $-234.70 | -7.2% | $765.30 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1410 | 51.1 | 49.6 | $-238.34 | -1.7% | $761.66 | -0.6 | done | can't tell from luck |
| value_ev10 | 779 | 38.1 | 39.3 | $-560.78 | -7.2% | $439.22 | -1.7 | done | can't tell from luck |
| trend_filter | 962 | 50.1 | 51.0 | $-576.82 | -6.0% | $423.18 | -1.9 | done | can't tell from luck |
| value_ev5 | 1169 | 40.4 | 41.2 | $-705.25 | -6.0% | $294.75 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1702 | 50.9 | 50.9 | $-752.00 | -4.4% | $248.00 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1702 | 49.1 | 50.0 | $-1009.75 | -5.9% | $-9.75 | -2.5 | done | losing for real |
| coinflip | 2408 | 50.0 | 50.5 | $-1195.92 | -5.0% | $-195.92 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1410 | 48.9 | 51.3 | $-1307.97 | -9.3% | $-307.97 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2408 | 50.2 | 51.8 | $-1580.55 | -6.6% | $-580.55 | -3.3 | done | losing for real |
| always_up | 2408 | 47.1 | 49.8 | $-2260.25 | -9.4% | $-1260.25 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3793 | 48.0 | 49.2 | $-2502.88 |
| ETH | 4159 | 47.9 | 48.6 | $-2748.82 |
| SOL | 4338 | 47.9 | 48.7 | $-2930.93 |
| XRP | 4394 | 48.5 | 48.6 | $-2239.70 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
