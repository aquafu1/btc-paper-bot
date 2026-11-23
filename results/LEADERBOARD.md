# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1214 windows, 33371 settled trades, 304 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1596 | 38.7 | 39.2 | $-781.50 | -4.9% | $218.50 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3344 | 50.8 | 50.3 | $-1064.90 | -3.2% | $-64.90 | -1.8 | done | can't tell from luck |
| value_ev5 | 2413 | 40.5 | 41.1 | $-1209.84 | -5.0% | $-209.84 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2798 | 49.5 | 49.4 | $-1285.71 | -4.6% | $-285.71 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2798 | 50.5 | 51.1 | $-1649.23 | -5.9% | $-649.23 | -3.2 | done | losing for real |
| trend_filter | 1972 | 48.7 | 50.4 | $-1682.81 | -8.5% | $-682.81 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3344 | 49.2 | 50.2 | $-2073.21 | -6.2% | $-1073.21 | -3.6 | done | losing for real |
| coinflip | 4818 | 50.0 | 50.1 | $-2210.97 | -4.6% | $-1210.97 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4818 | 50.2 | 51.4 | $-2936.16 | -6.1% | $-1936.16 | -4.4 | done | losing for real |
| always_up | 4818 | 47.9 | 49.3 | $-3508.75 | -7.3% | $-2508.75 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7719 | 48.1 | 48.9 | $-4310.71 |
| ETH | 8342 | 48.0 | 48.3 | $-4951.57 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
