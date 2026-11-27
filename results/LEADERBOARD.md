# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 12:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1600 windows, 38750 settled trades, 411 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 817 | 34.4 | 35.1 | $-605.00 | -7.4% | $395.00 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3824 | 50.9 | 50.0 | $-976.75 | -2.6% | $23.25 | -1.6 | done | can't tell from luck |
| value_ev10 | 1932 | 38.4 | 39.0 | $-1045.86 | -5.4% | $-45.86 | -1.9 | done | can't tell from luck |
| value_ev5 | 2896 | 40.4 | 41.0 | $-1473.33 | -5.1% | $-473.33 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3204 | 51.0 | 50.9 | $-1484.05 | -4.6% | $-484.05 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3204 | 49.0 | 49.2 | $-1729.87 | -5.4% | $-729.87 | -3.0 | done | losing for real |
| trend_filter | 2279 | 48.5 | 50.4 | $-2030.99 | -8.9% | $-1030.99 | -4.4 | done | losing for real |
| coinflip | 5590 | 50.0 | 49.9 | $-2355.77 | -4.2% | $-1355.77 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3824 | 49.1 | 50.2 | $-2382.09 | -6.2% | $-1382.09 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 5590 | 50.1 | 51.3 | $-3516.40 | -6.3% | $-2516.40 | -4.8 | done | losing for real |
| always_up | 5590 | 48.2 | 49.1 | $-3597.52 | -6.4% | $-2597.52 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10307 | 47.9 | 48.6 | $-5860.48 |
| ETH | 11133 | 48.0 | 47.7 | $-5752.92 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
