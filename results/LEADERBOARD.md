# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 10:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1211 windows, 33324 settled trades, 268 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 651 | 34.4 | 35.3 | $-458.79 | -7.0% | $541.21 | -1.4 | done | can't tell from luck |
| value_ev10 | 1593 | 38.7 | 39.2 | $-799.96 | -5.0% | $200.04 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3340 | 50.8 | 50.3 | $-1111.34 | -3.3% | $-111.34 | -1.9 | done | can't tell from luck |
| value_ev5 | 2409 | 40.5 | 41.1 | $-1218.30 | -5.1% | $-218.30 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2793 | 49.5 | 49.4 | $-1301.34 | -4.7% | $-301.34 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2793 | 50.5 | 51.1 | $-1641.55 | -5.9% | $-641.55 | -3.2 | done | losing for real |
| trend_filter | 1969 | 48.7 | 50.4 | $-1675.92 | -8.5% | $-675.92 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3340 | 49.2 | 50.2 | $-2033.21 | -6.1% | $-1033.21 | -3.6 | done | losing for real |
| coinflip | 4812 | 50.0 | 50.1 | $-2191.25 | -4.6% | $-1191.25 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4812 | 50.3 | 51.4 | $-2899.28 | -6.0% | $-1899.28 | -4.3 | done | losing for real |
| always_up | 4812 | 47.9 | 49.3 | $-3491.07 | -7.3% | $-2491.07 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7697 | 48.1 | 48.9 | $-4328.59 |
| ETH | 8317 | 48.1 | 48.3 | $-4909.20 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
