# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 10:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 778 windows, 21487 settled trades, 31 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 404 | 32.9 | 34.9 | $-391.45 | -9.7% | $608.55 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 1819 | 50.0 | 49.6 | $-709.12 | -3.9% | $290.88 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2195 | 51.0 | 50.6 | $-734.23 | -3.3% | $265.77 | -1.6 | done | can't tell from luck |
| trend_filter | 1266 | 50.2 | 50.8 | $-742.42 | -5.9% | $257.58 | -2.1 | done | losing for real |
| value_ev10 | 982 | 37.4 | 39.1 | $-774.62 | -7.9% | $225.38 | -2.0 | done | losing for real |
| value_ev5 | 1486 | 39.8 | 41.0 | $-992.25 | -6.7% | $7.75 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1819 | 50.0 | 51.2 | $-1268.12 | -7.0% | $-268.12 | -3.0 | done | losing for real |
| coinflip | 3107 | 50.2 | 50.3 | $-1329.05 | -4.3% | $-329.05 | -2.4 | done | losing for real |
| momentum_15m_0.10pct | 2195 | 49.0 | 50.2 | $-1399.30 | -6.4% | $-399.30 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 3107 | 51.2 | 51.7 | $-1408.16 | -4.5% | $-408.16 | -2.6 | done | losing for real |
| always_up | 3107 | 47.2 | 49.5 | $-2770.86 | -8.9% | $-1770.86 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4875 | 48.2 | 49.1 | $-2909.14 |
| ETH | 5366 | 48.0 | 48.5 | $-3567.52 |
| SOL | 5595 | 48.1 | 48.6 | $-3234.25 |
| XRP | 5651 | 48.5 | 48.5 | $-2808.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
