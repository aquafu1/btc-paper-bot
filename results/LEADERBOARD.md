# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 2:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1225 windows, 33548 settled trades, 417 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 655 | 34.4 | 35.3 | $-473.45 | -7.2% | $526.55 | -1.4 | done | can't tell from luck |
| value_ev10 | 1604 | 38.7 | 39.2 | $-786.99 | -4.9% | $213.01 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3364 | 50.8 | 50.3 | $-1103.82 | -3.3% | $-103.82 | -1.9 | done | can't tell from luck |
| value_ev5 | 2424 | 40.5 | 41.1 | $-1222.22 | -5.0% | $-222.22 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2814 | 49.5 | 49.4 | $-1300.50 | -4.6% | $-300.50 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2814 | 50.5 | 51.1 | $-1661.99 | -5.9% | $-661.99 | -3.2 | done | losing for real |
| trend_filter | 1983 | 48.8 | 50.5 | $-1670.71 | -8.4% | $-670.71 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3364 | 49.2 | 50.2 | $-2073.87 | -6.2% | $-1073.87 | -3.6 | done | losing for real |
| coinflip | 4842 | 50.0 | 50.1 | $-2230.20 | -4.6% | $-1230.20 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4842 | 50.3 | 51.4 | $-2930.70 | -6.1% | $-1930.70 | -4.3 | done | losing for real |
| always_up | 4842 | 47.9 | 49.3 | $-3529.81 | -7.3% | $-2529.81 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7810 | 48.1 | 48.9 | $-4433.44 |
| ETH | 8428 | 48.1 | 48.3 | $-4966.58 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
