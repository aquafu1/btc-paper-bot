# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 2:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1608 windows, 38854 settled trades, 406 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 820 | 34.3 | 35.1 | $-635.00 | -7.7% | $365.00 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3835 | 50.9 | 50.0 | $-993.42 | -2.6% | $6.58 | -1.6 | done | can't tell from luck |
| value_ev10 | 1940 | 38.4 | 39.0 | $-1055.80 | -5.4% | $-55.80 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 3209 | 51.0 | 50.9 | $-1492.17 | -4.6% | $-492.17 | -2.7 | done | losing for real |
| value_ev5 | 2905 | 40.4 | 41.0 | $-1493.27 | -5.1% | $-493.27 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 3209 | 49.0 | 49.2 | $-1723.64 | -5.4% | $-723.64 | -3.0 | done | losing for real |
| trend_filter | 2283 | 48.5 | 50.4 | $-2033.23 | -8.9% | $-1033.23 | -4.4 | done | losing for real |
| coinflip | 5606 | 50.1 | 49.9 | $-2318.99 | -4.1% | $-1318.99 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3835 | 49.1 | 50.2 | $-2369.91 | -6.2% | $-1369.91 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5606 | 50.1 | 51.3 | $-3498.41 | -6.2% | $-2498.41 | -4.8 | done | losing for real |
| always_up | 5606 | 48.2 | 49.1 | $-3569.18 | -6.4% | $-2569.18 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10355 | 48.0 | 48.6 | $-5836.96 |
| ETH | 11189 | 48.0 | 47.7 | $-5761.83 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
