# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 1:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1511 windows, 37582 settled trades, 386 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 764 | 34.6 | 35.4 | $-548.45 | -7.2% | $451.55 | -1.5 | done | can't tell from luck |
| value_ev10 | 1836 | 38.6 | 39.2 | $-928.95 | -5.1% | $71.05 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3739 | 50.9 | 50.1 | $-967.90 | -2.6% | $32.10 | -1.6 | done | can't tell from luck |
| value_ev5 | 2767 | 40.6 | 41.1 | $-1326.82 | -4.8% | $-326.82 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3136 | 51.1 | 51.0 | $-1424.29 | -4.5% | $-424.29 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3136 | 48.9 | 49.2 | $-1720.56 | -5.5% | $-720.56 | -3.1 | done | losing for real |
| trend_filter | 2226 | 48.6 | 50.3 | $-1912.55 | -8.6% | $-912.55 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3739 | 49.1 | 50.2 | $-2300.85 | -6.2% | $-1300.85 | -3.8 | done | losing for real |
| coinflip | 5413 | 50.0 | 50.0 | $-2370.93 | -4.4% | $-1370.93 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5413 | 50.2 | 51.3 | $-3314.85 | -6.1% | $-2314.85 | -4.6 | done | losing for real |
| always_up | 5413 | 48.1 | 49.2 | $-3553.40 | -6.6% | $-2553.40 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9757 | 48.0 | 48.7 | $-5357.99 |
| ETH | 10515 | 48.1 | 47.9 | $-5427.32 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
