# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 8:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1248 windows, 33866 settled trades, 415 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 664 | 34.2 | 35.3 | $-514.16 | -7.7% | $485.84 | -1.5 | done | can't tell from luck |
| value_ev10 | 1624 | 38.4 | 39.2 | $-900.67 | -5.5% | $99.33 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3394 | 50.9 | 50.3 | $-1070.81 | -3.2% | $-70.81 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2839 | 49.5 | 49.4 | $-1332.61 | -4.7% | $-332.61 | -2.5 | done | losing for real |
| value_ev5 | 2452 | 40.2 | 41.1 | $-1374.34 | -5.6% | $-374.34 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2839 | 50.5 | 51.1 | $-1653.84 | -5.8% | $-653.84 | -3.2 | done | losing for real |
| trend_filter | 2002 | 48.7 | 50.4 | $-1710.75 | -8.5% | $-710.75 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3394 | 49.1 | 50.2 | $-2143.38 | -6.3% | $-1143.38 | -3.7 | done | losing for real |
| coinflip | 4886 | 50.0 | 50.1 | $-2213.75 | -4.5% | $-1213.75 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4886 | 50.3 | 51.4 | $-2959.17 | -6.1% | $-1959.17 | -4.4 | done | losing for real |
| always_up | 4886 | 47.9 | 49.3 | $-3585.90 | -7.3% | $-2585.90 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7963 | 47.9 | 48.9 | $-4804.61 |
| ETH | 8593 | 48.1 | 48.3 | $-5070.55 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
